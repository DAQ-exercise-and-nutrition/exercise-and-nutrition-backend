import sys
from flask import abort, request
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME
from urllib.parse import unquote

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)


def get_exercises():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("SELECT name, body_part, equipment, target, instructions FROM Exercise")
        results = cs.fetchall()
        return [
            {
                "name": row[0],
                "body_part": row[1],
                "equipment": row[2],
                "target": row[3],
                "instructions": row[4]
            }
            for row in results
        ]


def get_exercises_by_body_part(body_part):
    decoded_body_part = unquote(body_part)

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT name, body_part, equipment, target, instructions
            FROM Exercise
            WHERE body_part = %s
        """, [decoded_body_part])
        results = cs.fetchall()
        return [
            {
                "name": row[0],
                "body_part": row[1],
                "equipment": row[2],
                "target": row[3],
                "instructions": row[4]
            }
            for row in results
        ]


def get_exercises_by_target(target):
    decoded_target = unquote(target)

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT name, body_part, equipment, target, instructions
            FROM Exercise
            WHERE target = %s
        """, [decoded_target])
        results = cs.fetchall()
        return [
            {
                "name": row[0],
                "body_part": row[1],
                "equipment": row[2],
                "target": row[3],
                "instructions": row[4]
            }
            for row in results
        ]


def get_foods():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("SELECT name, diet, meal_type, cal, fat, carb, protein FROM Food")
        results = cs.fetchall()
        return [
            {
                "name": row[0],
                "diet": row[1],
                "meal_type": row[2],
                "cal": row[3],
                "fat": row[4],
                "carb": row[5],
                "protein": row[6]
            }
            for row in results
        ]


def get_foods_by_diet(diet):
    decoded_diet = unquote(diet)

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT name, diet, meal_type, cal, fat, carb, protein
            FROM Food
            WHERE diet = %s
        """, [decoded_diet])
        results = cs.fetchall()
        return [
            {
                "name": row[0],
                "diet": row[1],
                "meal_type": row[2],
                "cal": row[3],
                "fat": row[4],
                "carb": row[5],
                "protein": row[6]
            }
            for row in results
        ]


def get_foods_by_meal_type(meal_type):
    decoded_meal_type = unquote(meal_type)

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT name, diet, meal_type, cal, fat, carb, protein
            FROM Food
            WHERE meal_type = %s
        """, [decoded_meal_type])
        results = cs.fetchall()
        return [
            {
                "name": row[0],
                "diet": row[1],
                "meal_type": row[2],
                "cal": row[3],
                "fat": row[4],
                "carb": row[5],
                "protein": row[6]
            }
            for row in results
        ]
