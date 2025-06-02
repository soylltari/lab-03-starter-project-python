from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get('/matrix-multiply')
def matrix_multiply() -> dict:
    """
    Генерує 2 випадкові матриці 10x10 та перемножує їх між собою.
    
    Returns:
        dict: Словник з матрицями A, B та їх добутком
    """
    matrix_a = np.random.rand(10, 10)
    matrix_b = np.random.rand(10, 10)
    
    result = np.dot(matrix_a, matrix_b)
    
    return {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(), 
        "result": result.tolist()
    }