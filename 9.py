candidate_count = int(input())
voices = dict()


while candidate_count > 0:
    candidate_count -= 1
    state_voices = input().split()
    if state_voices[0] in voices:
        voices[state_voices[0]] += int(state_voices[1])
    else:
        voices[state_voices[0]] = int(state_voices[1])

print("\nOutput:")
for key, value in voices.items():
    print(f"{key} {value}")