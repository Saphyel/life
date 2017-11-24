"""
Check if applies the rules of the game
"""
# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, then, when
from life.universe import Universe
from life.cell import Cell


@given('a universe with only {quantity} cells')
def step_impl(context, quantity):
    context.universe = Universe()
    for pos in range(int(quantity)):
        cell = Cell(pos, pos)
        context.universe.add_cell(cell)


@given('a universe with a block of {quantity_x} x {quantity_y} cells')
def step_impl(context, quantity_x, quantity_y):
    context.universe = Universe()
    for pos_x in range(int(quantity_x)):
        for pos_y in range(int(quantity_y)):
            cell = Cell(pos_x, pos_y)
            context.universe.add_cell(cell)


@when('you add more cells')
def step_impl(context):
    context.universe.count_neighbours()
    assert context.universe.get_cells()[0].is_alive() is False
    context.universe.add_cell(Cell(2, 1))
    context.universe.add_cell(Cell(1, 2))


@then('the cell {quantity} is dead')
def step_impl(context, quantity):
    context.universe.count_neighbours()
    assert context.universe.get_cells()[int(quantity)].is_alive() is False


@then('the cell {quantity} is alive')
def step_impl(context, quantity):
    context.universe.count_neighbours()
    assert context.universe.get_cells()[int(quantity)].is_alive() is True
