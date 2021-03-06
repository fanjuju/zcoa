import logging.handlers
class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 创建一个日志器
            cls.logger = logging.getLogger()
            # 日志器设置级别
            cls.logger.setLevel(logging.INFO)
            # 日志信息打印到控制台
            # ch = logging.StreamHandler()
            # cls.logger.addHandler(ch)
            # 创建一个样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            # 创建一个格式器，并将样式添加到格式器中
            fm = logging.Formatter(fmt)
            # 创建一个处理器
            tf = logging.handlers.TimedRotatingFileHandler(filename='../logger/test.log',
                                                           when='H',
                                                           interval= 1,
                                                           backupCount= 3,
                                                           encoding= 'utf-8')
            # 格式器添加到处理器中
            tf.setFormatter(fm)
            # 将格式器添加到日志器中
            cls.logger.addHandler(tf)
        return cls.logger