import sys
from flask import abort, request
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME
from urllib.parse import unquote
import random

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)


def get_exercises(target=None, body_part=None, limit=None, randomize=False):
    sql_query = """
        SELECT name, body_part, equipment, target, instructions
        FROM Exercise
    """

    if target:
        sql_query += f" WHERE target = '{target}'"
    elif body_part:
        sql_query += f" WHERE body_part = '{body_part}'"

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(sql_query)
        results = cs.fetchall()

    if randomize:
        random.shuffle(results)

    if limit:
        results = results[:limit]

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


def get_exercises_by_body_part(body_part, limit=None, randomize=False):
    sql_query = f"""
        SELECT name, body_part, equipment, target, instructions
        FROM Exercise
        WHERE body_part = '{body_part}'
    """

    if randomize:
        sql_query += " ORDER BY RAND()"

    if limit:
        sql_query += f" LIMIT {limit}"

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(sql_query)
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


def get_exercises_by_target(target, limit=None, randomize=False):
    sql_query = f"""
        SELECT name, body_part, equipment, target, instructions
        FROM Exercise
        WHERE target = '{target}'
    """

    if randomize:
        sql_query += " ORDER BY RAND()"

    if limit:
        sql_query += f" LIMIT {limit}"

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(sql_query)
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


def get_foods(diet=None, meal_type=None, limit=None, randomize=False):
    sql_query = """
        SELECT name, diet, meal_type, cal, fat, carb, protein
        FROM Food
    """

    if diet:
        sql_query += f" WHERE diet = '{diet}'"
    elif meal_type:
        sql_query += f" WHERE meal_type = '{meal_type}'"

    if randomize:
        sql_query += " ORDER BY RAND()"

    if limit:
        sql_query += f" LIMIT {limit}"

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(sql_query)
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


def get_foods_by_diet(diet, limit=None, randomize=False):
    sql_query = f"""
        SELECT name, diet, meal_type, cal, fat, carb, protein
        FROM Food
        WHERE diet = '{diet}'
    """

    if randomize:
        sql_query += " ORDER BY RAND()"

    if limit:
        sql_query += f" LIMIT {limit}"

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(sql_query)
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


def get_foods_by_meal_type(meal_type, limit=None, randomize=False):
    sql_query = f"""
        SELECT name, diet, meal_type, cal, fat, carb, protein
        FROM Food
        WHERE meal_type = '{meal_type}'
    """

    if randomize:
        sql_query += " ORDER BY RAND()"

    if limit:
        sql_query += f" LIMIT {limit}"

    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(sql_query)
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


data = [
    {"name": "Exercise 1", "target": "abs"},
    {"name": "Exercise 2", "target": "abs"},
    {"name": "Exercise 3", "target": "abs"}
]

random.shuffle(data)
print(data)