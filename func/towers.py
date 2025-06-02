def hanoi_towers(n: int, source: str, auxiliary: str, target: str) -> None:
    if n > 0:
        hanoi_towers(n-1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        hanoi_towers(n-1, auxiliary, source, target)

def main():
    n = 3  
    hanoi_towers(n, 'A', 'B', 'C')

if __name__ == "__main__":
    main()
