using System;
using Entity;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Repository
{
    public class NotificationRepository : INotificationRepository
    {
        private DataAccessContext context;

        public NotificationRepository()
        {
            this.context = new DataAccessContext();
        }
        public List<Notification> GetAll()
        {
            return this.context.Notifications.ToList();
        }

        public Notification Get(int id)
        {
            return this.context.Notifications.Where<Notification>(x => x.Id == id).First<Notification>();
        }

        public void Insert(Notification notification)
        {
            try
            {
                this.context.Notifications.Add(notification);
                this.context.SaveChanges();
            }
            catch(Exception ex){
                throw ex;
            }
            
        }

        public void Delete(int id)
        {
            try
            {
                this.context.Notifications.Remove(this.Get(id));
                this.context.SaveChanges();
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        public void Update(Notification notification)
        {
            Notification updateNoti = this.Get(notification.Id);
            updateNoti.Status = "seen";
            this.context.SaveChanges();
        }

    }
}
