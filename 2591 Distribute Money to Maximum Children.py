def distMoney(self, money: int, children: int) -> int:
    if money < children: return -1
    money -= children  # now everybody has 1$
    good, rest = divmod(money, 7)
    if good > children:
        return children - 1
    if good == children:
        if rest == 0: return children
        else: return children - 1
    # good < children
    if good == children - 1 and rest == 3:
        return children - 2
    return good
