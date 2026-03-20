def solution(video_len, pos : str, op_start, op_end, commands):
    vlen = strtotime(video_len)
    curr = strtotime(pos)
    start = strtotime(op_start)
    end = strtotime(op_end)

    for comm in commands:
        if start <= curr <= end:
            curr = end
        if comm == "next":
            curr += 10
            if curr > vlen:
                curr = vlen                
        elif comm == "prev":
            curr -= 10
            if curr < 0:
                curr = 0
        if start <= curr <= end:
            curr = end

    mm = curr // 60
    ss = curr % 60

    if mm < 10:
        mm = f"0{mm}"
    if ss < 10:
        ss = f"0{ss}"

    answer = f"{mm}:{ss}"

    return answer

def strtotime(time : str):
    mm, ss = time.split(":")
    mm, ss = int(mm), int(ss)
    tt = mm * 60 + ss

    return tt