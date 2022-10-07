from abc import ABC, abstractmethod
from dataclasses import dataclass


class AuditTrail:
    def record(self) -> None:
        print('Audit')


@dataclass
class Task(ABC):
    audit_trail: AuditTrail = AuditTrail()

    def execute(self) -> None:
        self.audit_trail.record()
        self.do_execute()
        print('Transfer Money')

    @abstractmethod
    def do_execute(self) -> None:
        pass

class GenerateReportTask(Task):
    def do_execute(self) -> None:
        print('Generate Report')

class TransferMoneyTask(Task):
    def do_execute(self) -> None:
        print('Transfer Money')


if __name__ == '__main__':
    task = TransferMoneyTask()
    task.execute()
    # Audit
    # Transfer Money
