from download.data import DownloadData
from metadata.data import MetadataItem
from download.state import DownloadState

class DownloadTask:
    def __init__(self, data: DownloadData, item: MetadataItem):
        self.data = data
        self.item = item
        self.state = DownloadState.WAITING  # 초기 상태로 설정

    def start(self):
        self.state = DownloadState.RUNNING
        self.item.setDownloadState(self.state)
        # 필요 시, metadata_item에 상태를 전달하여 업데이트

    def pause(self):
        self.state = DownloadState.PAUSED
        self.data._pause_event.clear() # 대기 상태로 들어감
        self.item.setDownloadState(self.state)
        # metadata_item에 상태 전달

    def resume(self):
        self.state = DownloadState.RUNNING
        self.data._pause_event.set()
        self.item.setDownloadState(self.state)
        # 상태 업데이트 전달

    def stop(self, message:str):
        self.state = DownloadState.WAITING
        self.data._pause_event.set()
        self.item.setDownloadState(self.state, message)
        # 상태 업데이트 전달

    def finish(self):
        self.state = DownloadState.FINISHED
        self.item.setDownloadState(self.state)
        # 상태 업데이트 전달

    def isRunning(self):
        return self.state == DownloadState.RUNNING