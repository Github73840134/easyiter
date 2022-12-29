packet_size = 64
info_packet = False
__version__ = 1.0
def create_from_string(data):
	global packet_size,info_packet
	result = [""]
	index = 0
	pindex = 0
	if info_packet:
		result.append("")
		pindex += 1
	for i in data:
		if index == packet_size:
			pindex += 1
			if info_packet:
				result[0] = str(pindex)
			index = 0
			result.append("")
		result[pindex] += i
		index += 1
	return result
def create_from_bytes(data):
	global packet_size,info_packet
	result = [b""]
	index = 0
	pindex = 0
	if info_packet:
		result.append(b"")
		pindex += 1
	for i in data:
		if index == packet_size:
			pindex += 1
			if info_packet:
				result[0] = str(pindex)
			index = 0
			result.append(b"")
		result[pindex] += i
		index += 1
	return result
def join_from_string(data,info_packet=False):
	if info_packet:
		return "".join(data[1:])
	else:
		return "".join(data)
def join_from_bytes(data,info_packet=False):
	if info_packet:
		return b"".join(data[1:])
	else:
		return b"".join(data)