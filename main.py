#6
codes = [101, 102, 103, 104]
codes_copy = codes.copy()
codes.extend([105, 106])
codes_copy.insert(0, 100)
codes_copy.insert(0, 99)
codes.sort()
codes_copy.sort()
print(codes)
print(codes_copy)

#7
workers = ['Bob', 'Alice', 'Charlie', 'Dave']
workers.append('Eve')
workers.remove('Charlie')
workers.insert(workers.index('Alice'), 'Frank')
workers.sort()
print(workers)

#8
subjects = ['Biology', 'History', 'Geography']
subjects.extend(['Literature', 'Art'])
print(subjects.index('History'))
subjects.remove('Geography')
subjects_copy = subjects.copy()
print(subjects_copy)

#9
songs = ['pop', 'rock', 'jazz', 'rock', 'blues']
print(songs.count('rock'))
songs.pop()
songs.extend(['hiphop', 'classical'])
songs.sort()
print(songs)

#10
gadgets = ['phone', 'laptop', 'tablet', 'watch']
gadgets.insert(0, 'headphones')
gadgets.remove('laptop')
gadgets_copy = gadgets.copy()
gadgets_copy.append('camera')
gadgets.clear()
print(gadgets)
print(gadgets_copy)
