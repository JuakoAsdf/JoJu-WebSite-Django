$(function()
{
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
				'ÁÉÍÓÚáéíóú- ';	
			
		$('.txtNombre').keypress(function(e)
		{
			let caracter = String.fromCharCode(e.which);
			if(letras.indexOf(caracter)<0)
				return false;
		})
		
};

/*
$('.txtCodigo').keypress(function(e)
	{
		let caracter = String.fromCharCode(e.which);
		if(numeros.indexOf(caracter) < 0)
			return false;
	})
	*/