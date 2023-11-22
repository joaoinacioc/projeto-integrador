function confirmarExclusao() {
    var resposta = confirm("Tem certeza de que deseja excluir sua conta?");
    if (resposta) {
        // Se o usuário clicar em "OK", redirecione para a rota de exclusão
        window.location.href = urlExcluirConta;
    } else {
        window.location.href = cancelExConta;
    }
}

function confirmarExclusao() {
    var resposta = confirm("Tem certeza de que deseja excluir sua conta?");
    if (resposta) {
        // Se o usuário clicar em "OK", redirecione para a rota de exclusão
        window.location.href = urlExcluirConta;
    } else {
        exibirErro("Operação de exclusão cancelada.");
    }
}