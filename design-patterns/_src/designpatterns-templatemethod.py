from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class AuditTrail:
    def record(self) -> None:
        print('Audit')


@dataclass
class Task(metaclass=ABCMeta):
    __audit_trail: AuditTrail = AuditTrail()

    def execute(self) -> None:
        self.__audit_trail.record()
        print('Transfer Money')

    @abstractmethod
    def _do_execute(self) -> None:
        pass

class GenerateReportTask(Task):
    def _do_execute(self) -> None:
        print('Generate Report')

class TransferMoneyTask(Task):
    def _do_execute(self) -> None:
        print('Transfer Money')


if __name__ == '__main__':
    task = TransferMoneyTask()
    task.execute()
    # Audit
    # Transfer Money
