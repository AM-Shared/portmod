args = []
for port in range(40000, 41024 + 1):
    args.append(f"-p {port}:{port}")
print(" ".join(args))
