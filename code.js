let input = document.querySelectorAll('input')
let display = document.querySelectorAll('div')
let button = document.querySelectorAll('button')

console.log(input)
console.log(typeof(input[0].value))

display[0].innerHTML = input[0].value

let input_to_output = async function(){

    let val = input[0].value;
    let val1 = '/save?data=' + val
    //console.log(val1);

    let lets = await fetch(val1)
    let text = await lets.text()
    console.log(text)

    display[0].innerHTML = input[0].value

}


let load = async function (){
    let val = '/load'
    let lets = await fetch(val)
    let text = await lets.text()
    display[0].innerHTML = text
}

load()

button[0].addEventListener('click', input_to_output);
button[1].addEventListener('click', load);


// 영구적인 데이터 저장 후보

// 1. 파일
// 1.1. 저장 위치: index.html과 동일한 위치

// 2. 데이터 베이스
// 2.1. 저장 위치: 서버 

// 3. 다른 홈페이지
// 3.1. 저장 위치: 네이브 블로그, 깃허브, 페이스북(내 계정)
