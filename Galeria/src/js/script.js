function abrirModal(ator){

let titulo = document.getElementById("titulo")
let descricao = document.getElementById("descricao")
let obra = document.getElementById("obra")

if(ator === "ator1"){

titulo.innerText = "O Homem Amarelo (arte figurativa)"

descricao.innerText = "É uma pintura com cores fortes e traços marcantes, que não busca ser realista. A obra valoriza a expressão e emoção, sendo um exemplo do início do modernismo no Brasil."

obra.src = "../public/obra 1.PNG"

}

if(ator === "ator2"){

titulo.innerText = "O Navio (arte abstrata)"

descricao.innerText = "Escultura que representa os navios negreiros, lembrando o período da escravidão. A obra destaca a memória histórica e a importância da cultura afro-brasileira."

obra.src = "../public/obra.2.PNG"

}

if(ator === "ator3"){

titulo.innerText = "Meu Limão (arte abstrata)"

descricao.innerText = "Pintura com cores vibrantes e formas geométricas, inspirada na cultura brasileira. A obra mistura arte contemporânea com elementos decorativos e populares."

obra.src = "../public/obra3.PNG"

}

document.getElementById("modal").style.display = "block"

}

function fecharModal(){
document.getElementById("modal").style.display = "none"
}




