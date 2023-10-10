from flask import Flask
import psycopg2

app=Flask(__name__)
conn=psycopg2.connect(
    database="twitter_clone", 
    user="posgres",
    password="Kevin254",
    host="localhost",
    port="5432"
)