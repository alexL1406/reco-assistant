import time


class ServiceUnavailable(Exception):
    pass


class ServiceStructure(object):

    def __init__(self, services):

        self.name = ""
        self.isReady = False
        self.services = services

    def wait_service(self):

        init_time = time.time()
        delta = 0

        while not self.isReady and delta < 15:
            time.sleep(0.5)

            delta = time.time() - init_time

        if delta < 15:
            return True

        else:
            raise ServiceUnavailable("service " + self.name + " unavailable after 15 s")
