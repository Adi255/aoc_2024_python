from collections import deque

FREE_SPACE = "."


def load_disk_map(path):
    with open(path) as f:
        return f.read().strip()


def create_file_blocks(disk_map):
    blocks = []
    file_id = 0
    for idx in range(0, len(disk_map)):
        disk_map_val = int(disk_map[idx])
        if idx % 2 == 0:
            for _ in range(disk_map_val):
                blocks.append(str(file_id))
            file_id += 1
        else:
            for _ in range(disk_map_val):
                blocks.append(FREE_SPACE)
    return blocks


def create_sized_file_blocks(disk_map):
    blocks = []
    file_id = 0
    for idx in range(0, len(disk_map)):
        disk_map_val = int(disk_map[idx])
        if idx % 2 == 0:
            blocks.append((str(file_id), disk_map_val))
            file_id += 1
        else:
            if disk_map_val > 0:
                blocks.append((FREE_SPACE, disk_map_val))
    return blocks


def compact_blocks(block_list):
    free_space_indexes = [i for i, char in enumerate(block_list) if char == FREE_SPACE]
    free_space_deque = deque(free_space_indexes)
    for idx in range(len(block_list) - 1, 0, -1):
        char = block_list[idx]
        if char != FREE_SPACE:
            free_space_idx = free_space_deque.popleft()
            if free_space_idx < idx:
                block_list[free_space_idx] = char
                block_list[idx] = FREE_SPACE
            else:
                break
    return block_list


def compact_sized_blocks(sized_blocks):
    length = len(sized_blocks)
    i = length - 1
    while i > 0:
        block = sized_blocks[i]
        required_space = block[1]
        id = block[0]
        if required_space == 0:
            i -= 1
            continue
        if id == FREE_SPACE:
            i -= 1
            continue
        j = 0
        while j < i:
            if sized_blocks[j][0] != FREE_SPACE:
                j += 1
                continue
            free_space = sized_blocks[j][1]
            if free_space > required_space:
                sized_blocks.insert(j, block)
                sized_blocks[j + 1] = (FREE_SPACE, free_space - required_space)
                sized_blocks[i + 1] = (FREE_SPACE, required_space)
                i += 1
                break
            elif free_space == required_space:
                sized_blocks[j] = block
                sized_blocks[i] = (FREE_SPACE, required_space)
                break
            j += 1
        i -= 1
    return sized_blocks


def calculate_checksum(compacted):
    checksum = 0
    for i, n in enumerate(compacted):
        if n == FREE_SPACE:
            break
        checksum += i * int(n)
    return checksum


def calculate_whole_file_checksum(compacted_sized_blocks):
    checksum = 0
    idx = 0
    for block in compacted_sized_blocks:
        for _ in range(block[1]):
            if block[0] != FREE_SPACE:
                checksum += idx * int(block[0])
            idx += 1
    return checksum


if __name__ == '__main__':
    disk = load_disk_map("day8_input.txt")
    print("reading blocks")
    disk_blocks = create_file_blocks(disk)
    print("compacting")
    compacted_blocks = compact_blocks(disk_blocks)
    print("compacted")
    compacted_checksum = calculate_checksum(compacted_blocks)
    print(compacted_checksum)

    print("sized blocks")
    sized_blocks = create_sized_file_blocks(disk)
    print("compacting sized blocks")
    compacted_sized_blocks = compact_sized_blocks(sized_blocks)
    print("checksum for compacted sized blocks")
    whole_file_checksum = calculate_whole_file_checksum(compacted_sized_blocks)
    print(whole_file_checksum)
