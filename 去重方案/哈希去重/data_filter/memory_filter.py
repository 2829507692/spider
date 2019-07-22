from . import BaseFilter

class MemoryFilter(BaseFilter):

    def _get_storage(self):
        return set()

    def _save(self,hashvalue):

        return self.storage.add(hashvalue)

    def _is_exist(self,hashvalue):
        if hashvalue in self.storage:
            return True
        return False