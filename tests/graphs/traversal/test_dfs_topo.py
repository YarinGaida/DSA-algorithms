from src.graphs.traversal.dfs_topo import dfs_topo_formal

def test_topo_sort():
    print("\n--- Testing Formal DFS Topological Sort ---")
    
    dependencies = {
        'Underwear': ['Pants', 'Shoes'], 
        'Pants':     ['Belt', 'Shoes'],  
        'Belt':      ['Jacket'],         
        'Shirt':     ['Tie', 'Belt'],    
        'Tie':       ['Jacket'],
        'Jacket':    [],
        'Socks':     ['Shoes'],          
        'Shoes':     []
    }

    result = dfs_topo_formal(dependencies)
    
    print(f"Topological Order (S): {result}")
    
    assert result.index('Socks') < result.index('Shoes')
    assert result.index('Underwear') < result.index('Pants')
    assert result.index('Shirt') < result.index('Belt')
    
    print("Test Passed!")

if __name__ == "__main__":
    test_topo_sort()