const readline = require('readline').createInterface({
  input: process.stdin, 
  output: process.stdout
})

readline.question('input pascaLine', pascaLine =>{
  console.log(`This is your input: ${pascaLine}`)
  getPascaN(pascaLine)
})

function getPascaN(N){
  var arr = new Array(N)
  for(let i = 0 ; i < N; i++){
    arr[i] = new Array()
  }
  for(let a = 0; a < N; a++) {
    for(let b = 0; b <= a; b++){
      if(a === b || b === 0){
        arr[a][b] = 1
      } else {
        arr[a][b] = arr[a-1][b-1] + arr[a-1][b]
      }
    }
  }
  let printStr = ''
  for(let k=0 ;k<N; k++){
    printStr += arr[N-1][k] + ' '
  }
  console.log(printStr)
}
