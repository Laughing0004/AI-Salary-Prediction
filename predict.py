import joblib
import pandas as pd

model = joblib.load(
    'salary_prediction_pipeline.pkl'
)

sample = pd.DataFrame({
    'years_experience':[5],
    'benefits_score':[8],
    'remote_ratio':[100]
})

prediction = model.predict(sample)

print(prediction)