import fileinput
import itertools
import math
import operator


def convert(value):
    return "".join(f"{int(c, 16):04b}" for c in value)


def read(bits, n):
    return "".join(next(bits) for _ in range(n))


def parse_literal(bits):
    value = ""
    while True:
        prefix = read(bits, 1)
        value += read(bits, 4)
        if prefix == "0":
            return int(value, 2)


def parse_operator(bits):
    packets = []
    length_type = read(bits, 1)

    if length_type == "0":
        length = int(read(bits, 15), 2)
        sub = iter(read(bits, length))
        while True:
            try:
                bit = next(sub)
                packets.append(parse_packet(itertools.chain(bit, sub)))
            except StopIteration:
                break
    else:
        n_packets = int(read(bits, 11), 2)
        while len(packets) < n_packets:
            packets.append(parse_packet(bits))

    return packets


def parse_packet(bits):
    packet = {}
    packet["version"] = int(read(bits, 3), 2)
    packet["type"] = int(read(bits, 3), 2)

    if packet["type"] == 4:
        packet["value"] = parse_literal(bits)
    else:
        packet["packets"] = parse_operator(bits)

    return packet


def parse(value):
    bits = iter(convert(value))
    return parse_packet(bits)


def evaluate(packet):
    t = packet["type"]
    if t == 4:
        return packet["value"]

    values = map(evaluate, packet["packets"])

    reduce_op = {0: sum, 1: math.prod, 2: min, 3: max}
    bin_op = {5: operator.gt, 6: operator.lt, 7: operator.eq}

    if t in reduce_op:
        return reduce_op[t](values)
    return int(bin_op[t](*values))


if __name__ == "__main__":
    hex_value = next(fileinput.input()).strip()

    def sum_versions(packet):
        return packet["version"] + sum(map(sum_versions, packet.get("packets", [])))

    packet = parse(hex_value)
    print("Part 1:", sum_versions(packet))
    print("Part 2:", evaluate(packet))
