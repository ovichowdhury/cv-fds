using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Entity
{
    public class Notification
    {
        public Notification()
        {
            this.Status = "unseen";
        }

        [Key]
        public int Id { get; set; }

        [Required]
        public string ImageURL { get; set; }

        [Required]
        public float FireRate { get; set; }
        public float Temp { get; set; }
        public float SmokeRate { get; set; }
        public string Status { get; set; }

        [Required]
        public DateTime Time { get; set; }
    }
}
