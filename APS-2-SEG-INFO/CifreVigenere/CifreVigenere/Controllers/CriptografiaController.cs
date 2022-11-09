using CifreVigenere.Service.Interface;
using Microsoft.AspNetCore.Mvc;

namespace CifreVigenere.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class CriptografiaController : ControllerBase
    {

        private readonly ILogger<CriptografiaController> _logger;
        private readonly ICriptografiaService _criptografiaService;

        public CriptografiaController(ILogger<CriptografiaController> logger, ICriptografiaService criptografiaService)
        {
            _logger = logger;
            _criptografiaService = criptografiaService;
        }

        [HttpGet("[action]")]
        public string Criptografar([FromQuery] string mensagem, string chave)
        {
            return _criptografiaService.Criptografar(mensagem, chave);
        }

        [HttpGet("[action]")]
        public string Decriptografar([FromQuery] string cifra, string chave)
        {
            return _criptografiaService.Decriptografar(cifra, chave);
        }
    }
}