from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status, Depends
# from fastapi.params import Body
from typing import List, Dict
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from random import randint
from .utils import connect

# instanciate the  FastAPI
app = FastAPI()

# initializing the cursor object after a successful connection
def get_db_cursor():
    return connect()


class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    


# lets query all the posts
@app.get("/posts")
async def get_all_posts(db_cursor:RealDictCursor = Depends(get_db_cursor)):
    db_cursor.execute(''' SELECT * FROM posts; ''')
    posts = db_cursor.fetchall()
    print(posts)
    return posts


# get specific post
@app.get("/post/{id}")
async def get_single_post(id,db_cursor:RealDictCursor = Depends(get_db_cursor)):
    db_cursor.execute(f''' SELECT * FROM posts WHERE id ={int(id)}; ''')
    post = db_cursor.fetchone()
    return post


# add single post to the database
@app.post("/add_post")
async def add_single_post(post_data:Post, db_cursor:RealDictCursor = Depends(get_db_cursor)):
    try:
        db_cursor.execute(f''' INSERT INTO posts (title, content, published) 	VALUES ('{post_data.title}', '{post_data.content}', {post_data.published}) ''')
        db_cursor.connection.commit()

        return {'message' : 'Post added Successfully'}
    
    except Exception as e:
        # Rollback changes in case of an error
        db_cursor.connection.rollback()
        raise HTTPException(status_code=500, detail=f'Error Inserting data: {str(e)}')



@app.delete('/delete/{id}')
async def delete_post(id:int, db_cursor:RealDictCursor=Depends(get_db_cursor)):
    try:
        query = '''
            DELETE FROM posts WHERE id = %s RETURNING *;
            '''
        db_cursor.execute(query, (id,))

        deleted_post = db_cursor.fetchone()
        db_cursor.connection.commit()

        return {'message' : f'post deleted successfully'}

    except Exception as e:
        # rollback if an error occured
        db_cursor.connection.rollback()
        raise HTTPException(status_code=500, detail=f'There was an Error deleting that post')



# updating a post
@app.put('/update/{id}')
async def update_post(id: int, update_data: Post, db_cursor: RealDictCursor = Depends(get_db_cursor)):
    try:
        query = '''
            UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s;
            '''
        db_cursor.execute(query, (update_data.title, update_data.content, update_data.published, id))
        db_cursor.connection.commit()  # save the database after updating

        return {'message': f'Post with ID {id} updated successfully'}

    except Exception as e:
        # rollback in case of an error
        db_cursor.connection.rollback()
        raise HTTPException(status_code=500, detail='There was a problem while updating the post')
