import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree["type"] = "Inner"
    tree.loc[~tree.id.isin(tree.p_id), "type"] = "Leaf"
    tree.loc[tree.p_id.isnull(), "type"] = "Root"
    return tree[['id', 'type']]


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree['type'] = np.where(tree['p_id'].isna(), 'Root', np.where(tree['id'].isin(tree['p_id']), 'Inner', 'Leaf'))
    return tree[['id', 'type']]
