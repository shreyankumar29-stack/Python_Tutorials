//Example1
// function square(x)
// {
//     return x * x
// }

// var f = square

// console.log(square)
// console.log(f(5))

//Example2:
// function square(x)
// {
//     return x * x
// }

// function my_map(func, arr)
// {
//     result = []
//     for (var i = 0; i < arr.length; i++)
//     {
//         result.push(func(arr[i]))
//     }
//     return result
// }

// var squares= my_map(square, [1, 2, 3, 4, 5]) 
// console. log(squares) 
// function cube(x) 
// {
//     return x * x * x; 
// }

//Example 3:
// function logger(msg)
// {
//      function log_message()
//      { 
//         console.log('Log: ' + msg)
//      }
// return log_message
//     }
// log_hi = logger('Hi!') 
// log_hi()

//Example4:

function html_tag(tag)
{
    function wrap_text(msg){
        console.log('<' + tag + '>' + msg + '</' +tag+ '>')
    }
    return wrap_text
}

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headtine!')

print_p = html_tag('p') 
print_p('Test Paragraph!')
