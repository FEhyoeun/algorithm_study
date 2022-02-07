function solution(participant, completion) {
    const obj = {}

    for (let p of participant) {
        obj[p] = obj[p] ? obj[p] + 1 : 1; // 동명이인 표시하려고. obj[p]가 0이면(falsy면) 1이 들어갈 테고, 1이면(truty면) +1가 될 것
    }
    for (let c of completion) {
        obj[c] -= 1; // key 값이 완주자. 즉, 완주자의 value를 0으로 만듦.
    }
    for (let key in obj) { // 이걸 for..of로 바꾸면 obj is not iterable이 나옴
        if (obj[key] == 1) { // 위에서 완주한 사람의 value는 0으로 셋팅됨. 따라서 1이면 완주하지 못한 선수.
            return key; // key 값이 완주자니 return key;
        }
    }
}