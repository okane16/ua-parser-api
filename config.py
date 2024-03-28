class Config:
    DEBUG = False
    DEVELOPMENT = False
    CRSF_ENABLED = True
    ASSETS_DEBUG = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    TEMPLATE_AUTO_RELOAD = True
    ASSETS_DEBUG = True