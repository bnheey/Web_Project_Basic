// main.js 파일을 test 하는 파일
// 일반적인 파일명 : 테스트하는 파일.test.js - (ex) main.test.js
// 테스트 파일을 만들어, 필요한 테스트를 실행하면서 코딩하는 것이 더 견고한 코딩을 하는데에 도움이 된다.

function sum(num1, num2) {
    let result = num1 + num2
    console.log("result : ", result)
    return result
}

function testfunction(email){
    if(email.includes('@')){
        return true
    }
    else {
        return false
    }
}

test(
    'test name',
    function () {
        expect(sum(10, 20)).toBe(30)
    }
)

test(
    'test email',
    function (){
        expect(testfunction('test@test.com')).toBe(true)
    }
)

test(
    'test invalid email',
    function (){
        expect(testfunction('email')).toBe((false))
    }
)