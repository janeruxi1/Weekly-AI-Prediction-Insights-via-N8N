from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import pandas as pd

app = FastAPI()
class DatasetPayload(BaseModel):
    data: List[Dict[str, Any]]
    
@app.post("/analyze")
def analyze_dataset(payload: DatasetPayload):
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(payload.data)
    
    summary=df.describe(include='all').to_dict()
    
    # Perform basic analysis
    analysis= {
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "columns": df.columns.tolist(),
        "summary_statistics": summary
    }
    
    return analysis