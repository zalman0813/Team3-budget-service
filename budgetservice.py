from datetime import datetime
import calendar

class BudgetService(object):
    def query(self, start, end):
        if start > end:
            return 0

        begin_month = datetime.strftime(start, "%Y%m")
        end_month = datetime.strftime(end, "%Y%m")

        budgetsList = self.get_budgets()
        amount = 0
        for budget in budgetsList:
            budget_datetime = datetime.strptime(budget.yearMonth, "%Y%m")
            budget_day = calendar.monthrange(budget_datetime.year, budget_datetime.month)[1]

            if budget_datetime.year == start.year and budget_datetime.month == start.month and start.year == end.year and start.month == end.month:
                amount += round(budget.amount*(end.day - start.day + 1)/budget_day, 2)
                return amount

            if self.is_same_year_month(budget_datetime, start):
                amount += round(budget.amount * (budget_day - start.day + 1) / budget_day, 2)

            if budget.yearMonth > begin_month and budget.yearMonth < end_month:
                amount += budget.amount

            if budget_datetime.year == end.year and budget_datetime.month == end.month:
                amount += round(budget.amount * end.day  / budget_day, 2)

        return amount



    def is_same_year_month(self, budget_datetime, start):
        month = budget_datetime.year == start.year and budget_datetime.month == start.month
        return month

    def get_budgets(self):
        pass