from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from common.logger import logger
from api.routes import router as orquestrator_router
from middleware.error_handler import setup_error_handlers
from config.settings import settings
import uvicorn


log = logger("main")


def create_app() -> FastAPI:
    log.info("Initializing FastAPI application")

    app = FastAPI(
        title="Auto Line Feeding API",
        description="",
        docs_url="/orchestrator-docs",
    )

    setup_error_handlers(app)

    log.debug("Adding CORS middleware")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    log.debug("Registering orchestrator routes")
    app.include_router(
        orquestrator_router,
        prefix="/orchestrator"
    )

    return app


app = create_app()


if __name__ == "__main__":
    log.info("Starting Uvicorn server (127.0.0.1:8001, reload=True)")
    try:
        uvicorn.run(
            "main:app",
            host="127.0.0.1",
            port=8001,
            reload=True
        )
    except Exception as e:
        log.error(f"Uvicorn server failed: {str(e)}", exc_info=True)
        raise


# -- ROUTE FOR HEALTH CHECK --
@app.get("/health")
def health_check():
    return {"status": "healthy", "app": settings.APP_NAME}