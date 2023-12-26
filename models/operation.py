class Operation:
    def __init__(
            self,
            pk,
            date,
            state,
            operation_amount,
            description,
            from_,
            to,
   ):
        self.pk = pk
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to
