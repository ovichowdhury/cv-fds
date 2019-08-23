using Entity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Repository
{
    public interface INotificationRepository
    {
        List<Notification> GetAll();
        Notification Get(int id);
        void Insert(Notification notification);
        void Delete(int id);
        void Update(Notification notification);
    }
}
