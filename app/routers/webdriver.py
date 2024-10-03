from fastapi import APIRouter, HTTPException
from app.services.webdriver_manager import WebDriverManager

router = APIRouter()
webdriver_manager = WebDriverManager()

@router.post('/webdriver/create')
async def create_webdriver(browser_type: str = 'chrome'):
    driver_id, error = webdriver_manager.create_driver(browser_type)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return {'driver_id': driver_id}

@router.post('/webdriver/{driver_id}/action')
async def execute_action(driver_id: int, action: dict):
    driver = webdriver_manager.get_driver(driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail='实例未找到')
    # 根据action执行相应操作，例如打开网页、点击元素等
    # 示例：driver.get(action['url'])
    return {'status': 'success'}

@router.delete('/webdriver/{driver_id}')
async def close_webdriver(driver_id: int):
    webdriver_manager.close_driver(driver_id)
    return {'status': 'closed'}
