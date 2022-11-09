namespace CifreVigenere.Service.Interface
{
    public interface ICriptografiaService
    {
        string Criptografar(string mensagem, string chave);
        string Decriptografar(string cifra, string chave);
    }
}
