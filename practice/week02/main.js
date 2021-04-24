// 변수는 int, string 등의 자료형을 선언하지 않고, 모두 동일하게 let을 사용한다.
// (ex) let temp = false, let temp = 10
let temp = "test"
console.log(temp)

// 리스트 자료구조
let list = [10, 20, 30]
console.log(list[0]) // 인덱스도 사용 가능
console.log(list.length) // length 사용 가능 : 리스트 길이 출력

//딕셔너리 자료구조
let dict = {'김철수': 13, '이영애': 21}
console.log(dict['김철수'])

// 값을 바꾸지 못하는 상수, 주로 대문자로 선언함
const CONST_VALUE = 100
console.log('CONST_VALUE의 값', CONST_VALUE)


/* 이전에는 let 대신 var 사용

둘의 차이? hoisting

console.log(e)  >> undifined
var e = 100

let 은 언제 변수를 선언했는지 확인해 이후 개발, 잘못된걸 사용자에게 보여주지 않고 그냥 프로그램이 죽음
-> var은 버그를 발생시킬 확률이 높아 사용하지 않음.
 */

// 함수 - 이 파일 내에서만 유효
function sum(num1, num2) {
    let result = num1 + num2
    console.log("result : ", result)
    return result
}

// 외부 파일에서도 sum 함수 사용 가능하도록 변경
exports.sum = sum

console.log(sum(10, 20))

// 조건문
if (sum(10, 20) > 50) {
    // true 표현식
    console.log("true")
} else {
    // false 표현식
    console.log("false")
}

// 반복문
for (let i = 0; i <= 100; i++) {
    if (i % 2 == 0) {
        console.log(i)
    }
}

let list1 = [10, 20, 30, 40]
for (let i = 0; i < list1.length; i++) {
    console.log(list1[i])
}

for (let i of list1) {
    console.log(i)
}

let scores = [
    {'name': '철수', 'score': 90},
    {'name': '영희', 'score': 85},
    {'name': '민수', 'score': 70},
    {'name': '형준', 'score': 50},
    {'name': '기남', 'score': 68},
    {'name': '동희', 'score': 30},
]

for (let i = 0; i < scores.length; i++) {
    if (scores[i]['score'] > 50) {
        console.log(scores[i]["name"])
    }
}

function calculateSum(n) {
    let sum = 0
    for (let i = 1; i < n; i++) {
        sum += i
    }
    return sum
}

exports.calculateSum = calculateSum

function countBerry(basket) {
    // basket 변수는 리스트
    let count = 0
    for (let i = 0; i < basket.length; i++) {
        if (basket[i] === '딸기') {
            count += 1
        }
    }
    return count
}

exports.countBerry = countBerry // 함수 자체를 할당



// 미세먼지(PM10)의 값이 25 미만인 측정소(구 단위, MSRSTE_NM)와 미세먼지 수치를 출력하기
function countAir(cityAir) {
    let state = []
    for (let i = 0; i < cityAir.length; i++) {
        let isCleanAir = cityAir[i]["PM10"] < 25
        if (isCleanAir) {
            state.push(cityAir[i]['MSRSTE_NM'])
            console.log("미세먼지 수치가 25㎍/㎥ 보다 작은 구 :", cityAir[i]['MSRSTE_NM'] + ",", cityAir[i]['PM10'] + "㎍/㎥")
        }
    }
    return state
}

exports.countAir = countAir

function printAir() {
    let state = countAir(cityAir)
    console.log(state)
}