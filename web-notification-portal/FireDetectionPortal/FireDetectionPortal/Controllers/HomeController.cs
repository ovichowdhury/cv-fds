using System;
using Entity;
using Repository;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;


namespace FireDetectionPortal.Controllers
{
    public class HomeController : Controller
    {
        private INotificationRepository repo;
        public HomeController()
        {
            this.repo = new NotificationRepository();
        }
        //
        // GET: /Home/
        public ActionResult Index()
        {
            return View(this.GetLastUnseenNotification());
        }
        
        [NonAction]
        private Notification GetLastUnseenNotification()
        {
            List<Notification> allNoti = this.repo.GetAll();
            List<Notification> unseenNoti = allNoti.Where<Notification>(x => x.Status == "unseen").ToList();
            unseenNoti.OrderByDescending(x => x.Time);
            foreach (var n in unseenNoti)
            {
                this.repo.Update(n);
            }
            return unseenNoti.Count == 0 ? null : unseenNoti.First();
        }

        public ActionResult Archive()
        {
            return View(this.repo.GetAll().OrderByDescending(x => x.Time));
        }

        public ActionResult Delete(int id)
        {
            try
            {
                this.repo.Delete(id);
                return RedirectToAction("Archive");
            }
            catch (Exception)
            {
                return RedirectToAction("Archive");
            }
            
        }

	}
}