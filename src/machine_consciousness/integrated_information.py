import numpy as np
from scipy.stats import entropy

def phi(system):
    """
    Compute the integrated information (phi) of a system.
    
    Args:
        system (np.ndarray): A 2D array representing the system's state transitions.
    
    Returns:
        float: The integrated information (phi) of the system.
    """
    n = system.shape[0]  # Number of elements in the system
    
    # Compute the state transition probabilities
    p_sys = np.zeros((n, n))
    for i in range(n):
        p_sys[i] = system[i] / np.sum(system[i])
    
    # Compute the entropy of the system
    H_sys = entropy(p_sys.flatten())
    
    # Compute the minimum information partition (MIP)
    phi_min = np.inf
    for partition in generate_partitions(n):
        p_part = np.zeros((n, n))
        for i in range(len(partition)):
            for j in range(len(partition)):
                if i == j:
                    p_part[partition[i], partition[j]] = p_sys[partition[i], partition[j]]
                else:
                    p_part[partition[i], partition[j]] = np.sum(p_sys[partition[i], partition[j]])
        H_part = np.sum([entropy(p_part[partition[i], partition[i]].flatten()) for i in range(len(partition))])
        phi_part = H_sys - H_part
        phi_min = min(phi_min, phi_part)
    
    return phi_min

def generate_partitions(n):
    """
    Generate all possible partitions of a set of n elements.
    
    Args:
        n (int): The number of elements in the set.
    
    Yields:
        list: A partition of the set, represented as a list of lists.
    """
    if n == 1:
        yield [[0]]
    else:
        for partition in generate_partitions(n - 1):
            yield partition + [[n - 1]]
            for i in range(len(partition)):
                yield partition[:i] + [partition[i] + [n - 1]] + partition[i+1:]

def conscious_agent_index(system):
    """
    Compute the Conscious Agent Index (CAI) of a system.
    
    Args:
        system (np.ndarray): A 2D array representing the system's state transitions.
    
    Returns:
        float: The Conscious Agent Index (CAI) of the system.
    """
    phi_sys = phi(system)
    phi_min = min([phi(subsystem) for subsystem in generate_subsystems(system)])
    return (phi_sys - phi_min) / phi_sys

def generate_subsystems(system):
    """
    Generate all possible subsystems of a system.
    
    Args:
        system (np.ndarray): A 2D array representing the system's state transitions.
    
    Yields:
        np.ndarray: A subsystem of the original system.
    """
    n = system.shape[0]  # Number of elements in the system
    for i in range(1, 2**n):
        subsystem = np.zeros_like(system)
        for j in range(n):
            if i & (1 << j):
                subsystem[j] = system[j]
        yield subsystem