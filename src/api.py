from pydantic import BaseModel
from fastapi import FastAPI
from recommendation import recommend_models
app = FastAPI()

class UserPrompt(BaseModel):
    user_prompt: str

@app.post("/recommend_models/")
async def get_recommendations(data: UserPrompt):
    user_prompt = data.user_prompt
    recommendations = recommend_models(user_prompt)
    return recommendations


# from fastapi import FastAPI
# from pydantic import BaseModel
  # Import recommendation logic

# app = FastAPI()

# class RecommendationRequest(BaseModel):
#     user_prompt: str
#     start_index: int
#     num_recommendations: int

# @app.post("/recommend_models/")
# async def recommend_models_endpoint(request: RecommendationRequest):
#     try:
#         # Call the recommendation function with the request data
#         recommendations = recommend_models(
#             user_prompt=request.user_prompt,
#             start_index=request.start_index,
#             num_recommendations=request.num_recommendations
#         )

#         # Return recommendations as JSON response
#         return recommendations

#     except Exception as e:
#         return {"error": str(e)}
