namespace CifreVigenere.Service.Interface
{
    public class CriptografiaService : ICriptografiaService
    {
        public string Criptografar(string mensagem, string chave)
        {
            if (string.IsNullOrEmpty(mensagem) || string.IsNullOrEmpty(chave)) return "";

            var cifra = "";
            for (int i = 0, j = 0; i < mensagem.Length; i++, j++)
            {
                var letra = char.ToUpper(mensagem[i]);
                if (letra < 'A' || letra > 'Z') {
                    cifra += letra;
                    continue;
                }
                cifra += (char)((letra + char.ToUpper(chave[j % chave.Length]) - 2 * 'A') % 26 + 'A');
            }
            return cifra;
        }

        public string Decriptografar(string cifra, string chave)
        {
            if (string.IsNullOrEmpty(cifra) || string.IsNullOrEmpty(chave)) return "";

            var mensagem = "";
            for (int i = 0; i < cifra.Length; i++)
            {
                var letra = char.ToUpper(cifra[i]);
                if (letra < 'A' || letra > 'Z')
                {
                    mensagem += letra;
                    continue;
                }
                var cha = char.ToUpper(chave[i % chave.Length]);
                mensagem += (char)((26 - (cha % 65 - letra % 65)) % 26 + 65);
            }
            return mensagem;
        }
    }
}
