from dataclasses import dataclass


class AuditTrail:
    def record(self) -> None:
        print('Audit')


@dataclass
class TransferMoneyTask:
    audit_trail: AuditTrail

    def execute(self):
        self.audit_trail.record()
        print('Transfer Money')


@dataclass
class GenerateReportTask:
    audit_trail: AuditTrail

    def execute(self):
        self.audit_trail.record()
        print('Generate Report')


if __name__ == '__main__':
    audit_trail = AuditTrail()
    task = TransferMoneyTask(audit_trail)
    task.execute()
    # Audit
    # Transfer Money
