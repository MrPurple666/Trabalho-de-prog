    function tst(){

        numbers = document.getElementById('Numbers').value.split(' ')

        media = 0

        for (i in numbers) {
            a = numbers[i]
            media = media + parseInt(a)
        }

         for (i in impares) {
          if (numbers%2 == 1)
          numbers = impares
          impares = impares 
        }
        
        sorted = numbers.sort(function(a, b) {return b - a;});
        
        document.getElementById('Sorted').innerHTML = sorted
        document.getElementById('Media').innerHTML = media /numbers.length
       document.getElementById('impares').innerHTML = impares
