import numpy as np
import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

class Array_shape(BaseModel):
    array = np.array()

model_runner = bentoml.sklearn.get("mlzoomcamp_homework:latest").to_runner()


svc = bentoml.Service("homework_classifier", runners=[model_runner])


@svc.api(input=JSON(pydantic_model=Array_shape), output=JSON())
async def classify(application_data):
    prediction = await model_runner.async_run(application_data)
    print(prediction)
    result = prediction[0]

    return result