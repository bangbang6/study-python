let a = 'acf,adf,a_f,python'
//1. \w不包括& \n 空格 但是包括_下划线 相当于a[A-Za-z0-9_]f 就是单词数字下划线字符
// \s 匹配   \n 空格 \s 等等 但是没 & 叫做空白字符
//{n}里面填的数字表示连续几个匹配  {3,6}表示有6个连在一起就6个 最少3个 (越大越优先) 
//为什么越大越优先 因为贪婪策略 他会一直往后找符合条件的 直到遇到不符合的字符 所以会停
/*  a.replace(/[A-Za-z0-9_]+/g,function(){
    console.log(arguments)
})  */
//2.[]里只是一个字符 多个的话要在[]后加+
//必须设成一个变量才能往下走匹配到下一个
//3.''' 加上问号就是非贪婪模式 匹配到满足的条件就结束而不是继续查找下一个看是否符合'''
/* var b = 'abababa' 
console.log(b.match(/([A-Za-z0-9_]?)/g)) */


//4.数量词 *表示匹配前面的0次或者多次 就可以不用{}指定数字 +一次或者无限多次 ?表示匹配0次或者一次/*

//5 重要: ? 有两个作用 直接更在字符后面的是表示0-1 已经有啦数量词在加?表示非贪婪模式 所以  [1]??表示0-1匹配非贪婪 即0 一个都没有匹配

//6.''' 边界匹配  防止\d{4,8} qq9位也能配出前8位的bug ^\d{4,8}$即可'''
//7.()表示组的概念 (python){3,6}表示python重复3-6次 ()对应[] [] 表一个字符 ()表字符组
/* let pattern = /[A-Za-z0-9_]?/g
let matches = pattern.exec(a)
console.log(matches)
matches = pattern.exec(a)
console.log(matches)
matches = pattern.exec(a)
console.log(matches)
matches = pattern.exec(a)
console.log(matches)  */

function d(){
    var c = 10
    function b(x){
         return c+x
    }
    return  b
}
var c = 11
let f = d()
console.log(f(6))


function m(x){
    function b(y){
        var z = y + x
        x = z
        return z 
    }
    return b
}
var zz = m(0)
console.log(zz(1))
console.log(zz(2))