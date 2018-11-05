"""Demonstrate scoping."""

count = 0

def show_count():
    print("count = ", count);

def set_count(c):
    global count
    count = c


show_count()
set_count(2)
show_count()